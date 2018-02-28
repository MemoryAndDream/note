using UnityEngine;
using System.Collections;

public class isReady : MonoBehaviour {
	public GameObject road, bird;
	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
		if(Input.GetButtonDown("Fire1")){
			gameObject.SetActive(false);
			road.GetComponent<road>().isBegin = true;
			bird.GetComponent<Rigidbody2D>().isKinematic = false;
			bird.GetComponent<Animator>().enabled = false;
		}
	}
}
