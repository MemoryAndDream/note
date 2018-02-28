using UnityEngine;
using System.Collections;

public class road : MonoBehaviour {
	public float speed = 0.3f;
	public Transform trans;
	public Vector3 pos;
	public GameObject[] roads;
	public bool isBegin;
	public int idx;

	// Use this for initialization
	void Start () {
		trans = gameObject.transform;
		idx = 0;
		pos = trans.position;
		pos.x = -1.6f;
		trans.position = pos;
		isBegin = false;
	}
	
	// Update is called once per frame
	void Update () {
	 	Vector3 pos = trans.position;
		pos.x -= speed * Time.deltaTime;
		trans.position = pos;
		if(pos.x <= -1.6f - 3.35f*idx) {
			Vector3 pp = roads[idx%2].transform.position;
			pp.x += 3.35f;
			idx++;
			roads[idx%2].transform.position = pp;
			if(isBegin){
				roads[idx%2].GetComponent<roadGen>().gen();
			}
		}
	}

	public void  reset() {
		isBegin = false;
		roads[0].GetComponent<roadGen>().hidden();
		roads[1].GetComponent<roadGen>().hidden();
	}

}
