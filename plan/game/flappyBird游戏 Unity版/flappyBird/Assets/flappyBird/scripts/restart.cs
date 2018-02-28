using UnityEngine;
using System.Collections;

public class restart : MonoBehaviour {
	public Camera cam2d;
	public GameObject ready; //,score,road, bird, bird01;
	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
		if(Input.GetButtonDown("Fire1")){
			Collider2D h = Physics2D.OverlapPoint(cam2d.ScreenToWorldPoint(Input.mousePosition), (1<<LayerMask.NameToLayer("btn")));  
			if(h) {  
				gameObject.SetActive(false);
				Time.timeScale = 1; 
				ready.SetActive(true);
//				score.GetComponent<score>().reset();
//				road.GetComponent<road>().reset();
//				bird.GetComponent<bird>().reset();
//				bird01.GetComponent<clider>().reset();
				GameObject[] resets = GameObject.FindGameObjectsWithTag("needReset");
				foreach(GameObject r in resets) {
					r.BroadcastMessage("reset");
				}
			}  
		}
	}

	void stopped() {
		Time.timeScale = 0;
	}
}
