from database.DB_connect import DBConnect
from model.airport import Airport
from model.arco import Arco


class DAO():

    @staticmethod
    def getAllAirports():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * from airports a order by a.AIRPORT asc"""

        cursor.execute(query)

        for row in cursor:
            result.append(Airport(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodes(min, idmapAirports):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT a.ID, a.IATA_CODE, count(*) as N
                    FROM airports a, flights f
                    WHERE a.ID = f.DESTINATION_AIRPORT_ID or a.ID = f.ORIGIN_AIRPORT_ID
                    GROUP BY a.ID, a.IATA_CODE
                    HAVING N >= %s
                    ORDER BY N ASC"""

        cursor.execute(query, (min,))

        for row in cursor:
            result.append(idmapAirports[row["ID"]])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(idmapAirports):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID, count(*) as n
                        from flights f 
                        group by f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID
                        order by f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID 
                        """

        cursor.execute(query)

        for row in cursor:
            result.append(Arco(idmapAirports[row["ORIGIN_AIRPORT_ID"]],
                               idmapAirports[row["DESTINATION_AIRPORT_ID"]],
                               row["n"]))

        cursor.close()
        conn.close()
        return result


